import sys
def main():
    s = input().rstrip()
    nums = [ord(c)-ord("a") for c in s]
    if len(s) < 26:
        c = ""
        for x in range(26):
            f = True
            for y in nums:
                if x == y:
                    f = False
                    break
            if f:
                c = chr(x + ord("a"))
                break
        print(s+c)
    else:
        if s == "zyxwvutsrqponmlkjihgfedcba":
            print("-1")
        else:
            x = -1
            for i in reversed(range(25)):
                if nums[i] < nums[i+1]:
                    x = i
                    break
            p = 26
            for i in range(x+1, 26):
                if nums[x] < nums[i] and nums[i] < p:
                    p = nums[i]
            print(s[:x]+chr(p+ord("a")))

if __name__ == "__main__":
    main()