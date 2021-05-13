N = int(input())
sum = 0
for a in range(1,N):
    b = (N-0.5)//a
    sum += int(b)
print(sum)