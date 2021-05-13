N = int(input())
S =input()

al = [chr(ord('a') + i) for i in range(26)]
left =[]
right = []
for i in S:
    right.append(i)

ans = 0

for i in range(len(S)):
    left.append(right[0])
    right.pop(0)
    aaa = 0
    for i in al:
        if i in left and i in right:
            aaa += 1
    ans = max(ans,aaa)

print(ans)
