n = int(input())
apple = [4*i+7*j for i in range(100) for j in range(100)]
print("Yes" if n in apple else "No")