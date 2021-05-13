import sys
input = lambda: sys.stdin.readline().rstrip()

S = input()

f = int(S[:2])
s = int(S[2:])

if (f <= 0 and s > 12) or (f > 12 and s <= 0) or (f <= 0 and s <= 0) or (f > 12 and s > 12):
    print("NA")  
elif (f > 12 and 0 < s <= 12) or (f <= 0 and 0 < s <= 12):
    print("YYMM")
elif (0 < f <= 12 and s > 12) or (0 < f <= 12 and s <= 0):
    print("MMYY")
elif 0 < f <= 12 and 0 < s <= 12:
    print("AMBIGUOUS") 