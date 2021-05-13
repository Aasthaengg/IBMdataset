N=int(input())
MOD=10**9+7
#AAA AAC AAG AAT ACA ACC ACG! ACT AGA AGC! AGG AGT ATA ATC ATG ATT
#0   1   2   3   4   5   6    7   8   9    10  11  12  13  14  15

#CAA CAC CAG CAT CCA CCC CCG CCT CGA CGC CGG CGT CTA CTC CTG CTT
#16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31

#GAA GAC! GAG GAT GCA GCC GCG GCT GGA GGC GGG GGT GTA GTC GTG GTT
#32  33   34  35  36  37  38  39  40  41  42  43  44  45  46  47

#TAA TAC TAG TAT TCA TCC TCG TCT TGA TGC TGG TGT TTA TTC TTG TTT
#48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63
ans=[1]*64
ans[6]=0
ans[9]=0
ans[33]=0
for i in range(N-3):
  val=[0]*64
  for j in range(16):
    for k in range(4):
      val[4*j+k]=(ans[j]+ans[j+16]+ans[j+32]+ans[j+48])%MOD
  val[6]=0
  val[9]=0
  val[33]=0
  val[41]=(val[41]-ans[10])%MOD
  val[45]=(val[45]-ans[11])%MOD
  val[57]=(val[57]-ans[14])%MOD
  ans=val
print(sum(ans)%MOD)