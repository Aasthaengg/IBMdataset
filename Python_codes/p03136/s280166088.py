N = int(input())
L = sorted(list(map(int, input().split())))

max_length = L[-1]
sum_length = sum(L[0:len(L)-1])

print("Yes") if max_length < sum_length else print("No")
