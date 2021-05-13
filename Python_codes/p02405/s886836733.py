while True:
    oddline = ''
    evenline = ''
    h, w = map(int, raw_input().split())
    if h+w==0:
        break
    for y in xrange(w):
        if y%2==0:
            oddline += '#'
            evenline += '.'
        else:
            oddline += '.'
            evenline += '#'
    for x in xrange(h):
        if x%2==0:
            print oddline
        else:
            print evenline
    print ''