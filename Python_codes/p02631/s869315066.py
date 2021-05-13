n=int(input())
a=list(map(int,input().split()))

s=0
for _ in a:
    s = s ^ _

print(a[0] ^ s, end="")

for i in range(1,len(a)):
    print(" ",a[i] ^ s, end="")
print()