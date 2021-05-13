while 1:
    line=map(int,raw_input().split())
    if line==[0,0]:
        break
    else:
        op=sorted(line)
        print op[0],op[1]