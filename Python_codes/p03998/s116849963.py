def main():
    sa = list(input())
    sb = list(input())
    sc = list(input())
    nex = 'a'
    while True:
        if nex == 'a':
            if sa:
                nex = sa.pop(0)
            else:
                print('A')
                break
        if nex == 'b':
            if sb:
                nex = sb.pop(0)
            else:
                print('B')
                break
        if nex == 'c':
            if sc:
                nex = sc.pop(0)
            else:
                print('C')
                break
        

if __name__ == '__main__':
  main()