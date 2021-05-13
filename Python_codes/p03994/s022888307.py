from collections import defaultdict
def main():
    s = list(input())
    K = int(input())
    lowercase = [chr(i) for i in range(97, 97+26)]
    en = []
    for i in range(26):
        en.append(26-i)
    dic = defaultdict(int)

    for i,j in zip(lowercase,en):
        dic[i] = j

    for i in range(len(s)):
        if s[i]=="a":
            pass
        else:
            now = dic[s[i]]
            if now<=K:
                s[i]="a"
                K -= now
            else:
                pass
    K %= 26
    s[-1] = chr(ord(s[-1])+K)
    print("".join(s))

if __name__ == '__main__':
    main()