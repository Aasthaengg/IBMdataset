a=int(input())
b=[]
for _ in range(a):
    b.append(int(input()))
n=max(b)//2
print(sum(b)-n)