abcde=[int(input()) for i in range(5)]
k=int(input())
print("Yay!" if abcde[-1]-abcde[0]<=k else ":(")
