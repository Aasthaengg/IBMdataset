n = int(input())
ai = [int(i) for i in input().split()]

ans = len(set(ai))

if ans % 2 == 1:
    print(ans)
else:
    print(ans-1)