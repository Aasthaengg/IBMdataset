s = str(input())
w = int(input())
word = "".join(s[h] for h in range(0,len(s),w))
print(word)