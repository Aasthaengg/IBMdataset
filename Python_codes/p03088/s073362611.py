from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

n = inn()
h = {
 'AG':1,
 'CG':1,
 'AGG':0,
 'aGG':1,
 'ATG':0,
 'aTG':1,
 'GA':1,
 'gA':3,
 'AC':1,
 'aC':3,
 'AT':1,
 'AGT':0,
 'aGT':1,
 'agT':2
}
for i in range(2,n):
    g = {}
    g['AG'] = h['GA']+h['gA']
    g['CG'] = h['aC']
    g['AGG'] = h['AG']
    g['aGG'] = h['CG']+h['AGG']+h['aTG']+h['aGG']+h['ATG']
    g['ATG'] = h['AT']
    g['aTG'] = h['AGT']+h['aGT']+h['agT']
    g['GA'] = h['AG']+h['CG']+h['AGG']+h['aTG']+h['aGG']+h['ATG']
    g['gA'] = h['GA']+h['gA']+h['AC']+h['aC']+h['AT']+h['AGT']+ \
             h['aGT']+h['agT']
    g['AC'] = h['gA']
    g['aC'] = h['AC']+h['aC']+h['AT']+ \
             h['aGT']+h['agT'] + \
             h['CG']+h['aTG']+h['aGG']
    g['AT'] = h['GA']+h['gA']
    g['AGT'] = h['AG']
    g['aGT'] = h['CG']+h['AGG']+h['aTG']+h['aGG']+h['ATG']
    g['agT'] = h['AC']+h['aC']+h['AT']+h['AGT']+ \
             h['aGT']+h['agT']
    h = g
sm = 0
for k in h:
    sm = (sm+h[k])%R
print(sm)
