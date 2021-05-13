def solve():
    T = input()
    ans = ""
    for i in range(len(T)):
        if T[i] == "?":
            ans += "D"
        else:
            ans += T[i]
    
    print(ans)
            
if __name__ == '__main__':
    solve()