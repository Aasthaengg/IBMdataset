if __name__ =='__main__':
    S = input()
    st = 0
    ed = 0
    cnt = 0
    flag = True
    for i, s in enumerate(S):
        if s=='A' and flag:
            st = i
            flag = False
        if s=='Z':
            ed = i
            cnt = max(cnt, ed-st)
    
    print(cnt+1)