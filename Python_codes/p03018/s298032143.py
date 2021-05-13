def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    s = input()
    i = 0
    cc = output = 0
    while i < len(s)-1:
        if s[i] == 'A':
            cc += 1
            i += 1
        elif s[i] == 'B' and s[i+1] == 'C':
            output += cc
            i += 2
        else:
            cc = 0
            i += 1
    print(output)

    return

if __name__ == '__main__':
    main()
