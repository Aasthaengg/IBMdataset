def main():
    from bisect import bisect_right
    s=input()
    t=input()
    ls=len(s)
    lt=len(t)

    dic={i:[] for i in set(t)}
    for i in range(ls):
        st=s[i]
        if st in dic:
            dic[st].append(i)  

    cnt=0
    idx=-1
    for i in range(lt):
        st=t[i]
        if dic[st]==[]:
            print(-1)
            exit()

        tmp_idx=bisect_right(dic[st],idx)

        if tmp_idx==len(dic[st]):
            cnt+=1
            idx=dic[st][0]
        
        else:
            idx=dic[st][tmp_idx]
    
    print(cnt*ls+idx+1)  
 
if __name__=='__main__':
    main()