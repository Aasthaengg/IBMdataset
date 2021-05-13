N = list(input().split())

if N.count("1") == N.count("9") == N.count("7") == N.count("4") == 1:
    print("YES")
else:
    print("NO")