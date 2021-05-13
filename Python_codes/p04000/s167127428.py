H,W,N = map(int,input().split())
ab_list = [tuple(map(int,input().split())) for _ in range(N)]
table_dict = {}

diffs = [-1,0,1]
diff_tuples = [(a,b) for a in diffs for b in diffs]

for a, b in ab_list:
    for da,db in diff_tuples:
        if a+da in table_dict:
            row = table_dict[a+da]
            if b+db in row:
                row[b+db] += 1
            else:
                row[b+db] = 1
        else:
            table_dict[a+da] = {}
            table_dict[a+da][b+db] = 1

cnts = [0 for _ in range(10)]

for h,row in table_dict.items():
    for w,v in row.items():
        if 2 <= h <= H-1 and 2 <= w <= W-1:
            cnts[v] += 1

square_3x3 = (H-2) *(W-2)
cnts[0] = square_3x3 - sum(cnts[1:])

for cnt in cnts:
    print(cnt)