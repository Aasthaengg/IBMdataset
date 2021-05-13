def main():
    s=input()
    t=input()
    ans=[]
    for i in range(len(s)-len(t)+1):
        for j in range(len(t)):
            if len(s) <= i+j or (s[i+j] != t[j] and s[i+j] != "?"):
                break
        else:
            ans.append((s[:i]+t+s[i+j+1:]).replace("?", "a"))
    ans.sort()
    print(ans[0] if len(ans) > 0 else "UNRESTORABLE")
    
if __name__ == "__main__":
    main()