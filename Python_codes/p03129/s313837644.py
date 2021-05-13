input_string = input().split()
N = int(input_string[0])
K = int(input_string[1])

r = int(N / 2 + 0.5)

if (r >= K):
    print("YES")
else:
    print("NO")