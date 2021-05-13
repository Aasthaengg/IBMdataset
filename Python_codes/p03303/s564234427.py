def output(string, digit):
    _output=""
    for i in range(len(string)):
        if i%digit==0:
            _output=_output+string[i]
        else: pass
    return _output

s=str(input())
d=int(input())
print(output(s, d))