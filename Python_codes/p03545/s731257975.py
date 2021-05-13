if __name__ == '__main__':
    s = input()
    
    # + or - を入れる位置は間なので-1する
    n = len(s) - 1
    
    for i in range(1<<n):    #2**nと同じ
        ans = s[0]
        for j in range(n):
            #iはどこに＋を挿入するか jはsのこと
            if (i >> j & 1) :
                ans += "+"
            else:
                ans += "-"
            
            ans += s[j+1]
        if eval(ans) == 7:
            print(ans+"=7")
            break