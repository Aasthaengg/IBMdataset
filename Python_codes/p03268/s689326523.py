N,K = [int(x) for x in input().split()]
num0 = 0
num1 = 0
if(K%2 == 0):
    num1 = int(N/K)
    num0 = int(N/K*2)-num1
else:
    num1 = int(N/K)
print(num1**3+num0**3)
