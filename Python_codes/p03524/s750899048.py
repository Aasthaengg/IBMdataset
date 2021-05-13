S = input()
ABC = [S.count(s) for s in "abc"]
if max(ABC)- min(ABC) <= 1:
    print("YES")
else:print("NO")