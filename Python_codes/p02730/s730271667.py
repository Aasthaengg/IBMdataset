# coding: utf-8
# Your code here!
def main():
    s = input()
    n = len(s)
    s1 = s[:int((n-1)/2)]
    s2 = s[int((n+3)/2)-1:]
    
    for tmp in [s, s1, s2]:
        tmp_rev = tmp[::-1]
        # print(tmp, tmp_rev)
        if tmp != tmp_rev:
            print("No")
            break
    else:
        print("Yes")
    
main()