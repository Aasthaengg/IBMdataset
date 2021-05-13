def main():
    n,a,b,c,d=map(int, input().split())
    s = input()

    if("##" in s[a-1:c] or "##" in s[b-1:d]):return 0
    if(d>c):
        return 1
    else:
        if("..." in s[b-2:d+1]):
            return 1
        else:
            return 0

if __name__ == '__main__':
    k=main()
    if(k):
        print("Yes")
    else:
        print("No")
