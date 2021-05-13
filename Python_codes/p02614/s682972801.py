h,w,k = list(map(int, input().split()))
masu = [input() for _ in range(h)]
ans = 0

def count_num(m, target, goal):
    for i in range(h):
        count = sum(map(lambda x: x.count(target), m))
    
    return count == goal

def change_row(m, i_row_0):
    m[i_row_0] = 'r'*w    
    return m

def change_col(m, j_col_0):
    for i in range(h):
        if j_col_0 < w:
            m[i] = m[i][:j_col_0]+'r'+ m[i][j_col_0+1:]
    return m




for idx_h in range(2**h):
    for idx_w in range(2**w):
        m = masu.copy()
        for i_row, row in enumerate(m):
            if idx_h & (2 ** i_row) > 0:
                m = change_row(m, i_row)

            for j_col, col in enumerate(row):
                if idx_w & (2 ** j_col) > 0:
                    m = change_col(m, j_col)
        
        #print(m)
        if count_num(m, '#', k):
            ans += 1
        
print(ans)