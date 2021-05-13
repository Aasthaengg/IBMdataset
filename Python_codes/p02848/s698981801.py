N = int(input())
S = input()
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

s = ""
for c in S:
    for i, a in enumerate(ABC):
        if a == c:
            break
    s += ABC[(i+N)%26]

print(s)