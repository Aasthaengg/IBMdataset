from collections import defaultdict
def solve():
    S = input()
    counter = defaultdict(int)

    for ch in S:
        counter[ch] += 1
    
    vals = sorted([counter["a"],counter["b"],counter["c"]])

    if vals[1] - vals[0] <= 1 and vals[2] - vals[0] <= 1:
        print('YES')
    else:
        print('NO')
        
if __name__ == '__main__':
    solve()
