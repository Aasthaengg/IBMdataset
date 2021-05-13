n = int(input())
difficulties = list(map(int, input().split()))

difficulties.sort()
first_half = difficulties[:int(n/2)]
second_half = difficulties[int(n/2):]

ans = second_half[0] - first_half[-1]

print(ans)