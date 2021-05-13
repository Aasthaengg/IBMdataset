n, a, b, c, d = map(int, input().split())
s = input()

if c < d:
    print("Yes" if s[a - 1:d].count("##") == 0 else "No")
    #aからd-1までで二個あるとあうと
else:
    print("Yes" if s[a - 1:c].count("##") ==
          0 and s[b - 2:d + 1].count("...") > 0 else "No")
          #b-1からd+1までで飛び越すの


