n = int(input())
dic_a = {str(k):v for k,v in zip(range(10),'abcdefghij')}

def main(s):
    if len(s) < n:
        for ss in range(int(max(s))+2):
            main(s+str(ss))
    else:
        print(''.join([dic_a[x] for x in s]))
            
main('0')