from collections import Counter
N = int(input())
s = input()
cnt = Counter(s)
#print(cnt)
print("Yes" if cnt["R"] > cnt["B"] else "No")