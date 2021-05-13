from collections import Counter
N = int(input())
s = input()
counter = Counter(s)
if counter["R"] > counter["B"]:
    print("Yes")
else:
    print("No")