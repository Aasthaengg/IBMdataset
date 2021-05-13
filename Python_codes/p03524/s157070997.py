from collections import defaultdict
def main():
    dd = defaultdict(int)
    dd["a"]=0;
    dd["b"]=0;
    dd["c"]=0;
    s = input()
    for i in range(len(s)):
        dd[s[i]]+=1 
    
    res = list(dd.values())
    if max(res)-min(res)>1:
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    main()
