N = int(input())
S = input().split()

print("Three" if (len(set(S)) == 3) else "Four")
