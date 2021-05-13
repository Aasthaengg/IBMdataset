def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    sx, sy, tx, ty = map(int, input().split())
    direction = ['U', 'R', 'D', 'L']
    path = ['']*4
    def inverse(s):
        ret = ''
        for x in s:
            if x == 'U':
                ret += 'D'
            if x == 'R':
                ret += 'L'
            if x == 'D':
                ret += 'U'
            if x == 'L':
                ret += 'R'
        return ret

    path[0] = 'R'*(tx-sx)+'U'*(ty-sy)
    path[2] = 'L'+'U'*(ty-sy+1)+'R'*(tx-sx+1)+'D'
    path[1] = inverse(path[0])
    path[3] = inverse(path[2])
    print(''.join(path))
    
        
    
if __name__ == '__main__':
    main()