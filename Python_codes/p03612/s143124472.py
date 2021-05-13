n = int(input())
p = [int(i) for i in input().split()]
ans =0
check = 0
for n,i in enumerate(p):
    if n+1 == i and check == 0:
        ans += 1
        check =1
    elif n+1 == i and check == 1:
        check = 0
    else:
        check=0
print(ans)
