N = int(input())
As = list(map(int, input().split()))

first = sum([a*2 if i%2==0 else -a*2 for i, a  in enumerate(As)])//2
ans = [str(first)]
for i, a in enumerate(As[:-1]):
    ans.append(str((a*2)-first))
    first = (a*2)-first
print(' '.join(ans))