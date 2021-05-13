def sub_print(text, a, b):
    print(text[a:b])
    return text

def sub_reverse(text, a, b):
    return text[:a] + text[a:b][::-1] + text[b:]
def sub_replace(text, a, b, p):
    return text[:a] +p + text[b:]

func = {'print':sub_print, 'reverse':sub_reverse, 'replace':sub_replace}

text = input()
q = int(input())
for i in range(q):
    line = input().split()
    text = func[line[0]](text, int(line[1]), int(line[2]) + 1, *line[3:])