N=int(input())
ls =[]
for i in range(1,int(N**0.5)+1):
    if N%i == 0:
        a = i
        b = N//i
        ls.append((a-1)+(b-1))
print(min(ls))
