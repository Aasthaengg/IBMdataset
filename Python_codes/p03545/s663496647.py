# coding: utf-8
# Your code here!
def main():
    tmp = input()
    a = int(tmp[0])
    b = int(tmp[1])
    c = int(tmp[2])
    d = int(tmp[3])
    
    for i in range(2 ** 3):
        opt = []
        for j in range(3):
            if (i >> j) & 1:
                opt.append("+")
            else:
                opt.append("-")
        ans = int(tmp[0])
        for j, x in enumerate(tmp[1:]):
            if opt[j] == "+":
                ans += int(x)
            else:
                ans -= int(x)
        if ans == 7:
            print(tmp[0] + opt[0] + tmp[1] + opt[1] + tmp[2] + opt[2] + tmp[3] + "=7")
            break
    
main()