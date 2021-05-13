n, k = map(int, input().split())
scores = list(map(int, input().split()))
right = k
left = right - k + 1

while right < n:
    if scores[right] > scores[left-1]:
        print("Yes")
    else:
        print("No")

    right += 1
    left += 1