n = int(input())
p = list(map(int, input().split()))

ans = []

def judge(l):
    if l[0]<l[1]<l[2]:
        return True
    elif l[0]>l[1]>l[2]:
        return True
    else:
        return False

for i in range(n-2):
    ans.append(judge(p[i:i+3]))

print(sum(ans))