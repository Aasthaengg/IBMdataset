n = int(input())


def judge(x):
    i = 1
    ans = 0
    while i*i < x:
        if x%i == 0:
            ans+=1
            if (x//i)*i == x:
                ans += 1
        i+=1
    if ans == 8:
        return True
    else:
        return False

ans = 0

for i in range(1,n+1,2):
    if judge(i):
        ans += 1
print(ans)