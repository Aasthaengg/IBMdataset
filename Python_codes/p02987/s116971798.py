
from collections import Counter

def main():
    c = Counter(input())
    if len(c) == 2 and all(v == 2 for v in c.values()):
        print("Yes")
    else:
        print("No")


main()