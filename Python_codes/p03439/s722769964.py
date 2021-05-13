N = int(input())


def ask(i):
    print(i, flush=True)
    resp = input()
    if resp == 'Vacant':
        exit()
    return resp


def test(l, r, l_resp, r_resp):
    if l % 2 == r % 2:
        return l_resp == r_resp
    else:
        return l_resp != r_resp


resp = ask(0)

l = 0
r = N
l_resp = resp
r_resp = resp

for _ in range(19):
    m = (l+r)//2
    m_resp = ask(m)
    if test(l, m, l_resp, m_resp):
        l, l_resp = m, m_resp
    else:
        r, r_resp = m, m_resp
