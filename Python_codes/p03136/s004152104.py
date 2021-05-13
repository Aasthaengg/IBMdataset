num = int(input())
input_line = list(map(int,input().split(' ')))
input_line.sort()
large = input_line.pop(-1)
if(sum(input_line)>large):
    print('Yes')
else:
    print('No')
