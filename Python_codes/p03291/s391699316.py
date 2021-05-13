def main():
    S = input()
    
    mod = 10**9 + 7
    Ans = [[0,0,0,0,0]]
    import copy
    q = 1
    
    S = S[::-1]
    for i in range(len(S)):
        tmp = copy.deepcopy(Ans[i])
        if S[i] == "C":
            tmp[2] += q
            Ans.append(tmp)
        elif S[i] == "B":
            tmp[1] += q
            tmp[3] += tmp[2]
            tmp[3] %= mod
            Ans.append(tmp)
        elif S[i] == "A":
            tmp[0] += q
            tmp[4] += tmp[3]
            tmp[4] %= mod
            Ans.append(tmp)
        elif S[i] == "?":
            a,b,c,bc,abc = tmp
            Ans.append([(3*a+q)%mod, (3*b+q)%mod, (3*c+q)%mod, (3*bc+c)%mod, (3*abc+bc)%mod])
            q *= 3
            q %= mod
            
    print(Ans[-1][-1])
    
    
main()