def resolve():
    s = input()
    len(s)

    for i in range(len(s)):
        s = s[0 : -1]
        #print(f"{s} length is {len(s)}")
        if len(s) % 2 == 0:
            sa = s[0 : int(len(s)/2)]
            sb = s[int(len(s)/2) : ]
            #print(f"sa is {sa} \nsb is {sb}")
            if sa == sb:
                print(len(s))
                break
resolve()